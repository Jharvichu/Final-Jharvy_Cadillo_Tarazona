output "id_config_red" {
    value = null_resource.red_config.id
}

output "values" {
    value = {
        vpc_cidr = var.vpc_cidr
        zone = var.zone
    }
}

output "metadata_file" {
    value = local_file.metadata.filename
}