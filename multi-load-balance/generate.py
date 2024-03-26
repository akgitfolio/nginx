import jinja2

def generate_file(template_file, services, output_file):
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(template_file)

    output_text = template.render(services=services)

    try:
        with open(output_file, 'w') as f:
            f.write(output_text)
        print(f"{output_file} generated successfully: {output_file}")
    except Exception as e:
        print(f"Error occurred while writing {output_file}: {e}")

def main():
    services = []
    start_port = 3001
    num_services = 10

    for i in range(num_services):
        service = {
            'name': f'server-{i+1}',
            'context': f'./server{i+1}',
            'host_port': start_port + i ,
            'container_port': start_port + i ,
        }
        services.append(service)

    generate_file('docker-compose.yml.j2', services, 'docker-compose.yml')
    generate_file('nginx.conf.j2', services, 'nginx.conf')

if __name__ == "__main__":
    main()
