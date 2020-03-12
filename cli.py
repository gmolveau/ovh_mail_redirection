import click
import json
import ovh
import random
import string

client = ovh.Client()

@click.command(name="list")
@click.argument('domain')
def list_command(domain):
    """Get all redirections for this domain"""
    redirection_ids = client.get('/email/domain/{}/redirection'.format(domain))
    for redirection_id in redirection_ids:
        r = client.get('/email/domain/{}/redirection/{}'.format(domain, redirection_id))
        print(json.dumps(r, indent=4))

@click.command(name='generate')
@click.argument('service', required=False)
# optional argument, required is False by default
def generate(service):
    """generate a random string"""
    r = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))
    if service:
        print("{}-{}".format(service, r))
    else:
        print(r)

@click.command(name='add')
@click.option('-D', '--domain', 'domain', required=True)
@click.option('-s', '--source', 'source_mail', required=True)
@click.option('-d', '--destination_mail', 'destination_mail', required=True)
def add(domain, source_mail, destination_mail):
    """Add a redirection"""
    result = client.post('/email/domain/{}/redirection'.format(domain),
        _from=source_mail,
        localCopy=False,
        to=destination_mail,
    )
    print(json.dumps(result, indent=4))

@click.command(name='web')
@click.option('-p', '--port', 'port', required=False)
# optional argument, required is False by default
def web(port):
    """start the web-ui"""
    pass

@click.group()
def cli():
    """Command line interface for the ovh-redirection package"""
    pass

cli.add_command(add)
cli.add_command(generate)
cli.add_command(list_command)
cli.add_command(web)

def main():
    cli()

if __name__ == '__main__':
    main()
