resource "null_resource" "red_config" {
    triggers = {
        name = var.name
        vpc_cidr = var.vpc_cidr
        zone = var.zone
    }

    provisioner "local-exec" {
      command = <<-EOT
        echo "Configuracion de la red ${var.name}:"
        echo "VPC DICR : ${var.vpc_cidr}"
        echo "Zona disponible : ${var.zone}"
      EOT
    }   
}

resource "local_file" "metadata" {
    content  = jsonencode({
        name = null_resource.red_config.triggers.name,
        cidr = null_resource.red_config.triggers.vpc_cidr,
        zone = null_resource.red_config.triggers.zone
    })
    filename = "${path.module}/network_metadata.json"
}
