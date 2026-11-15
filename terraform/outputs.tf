output "kubernetes_namespace" {
  value = kubernetes_namespace.homework.metadata[0].name
}

output "helm_release_name" {
  value = helm_release.homework.name
}

output "helm_app_version" {
  value = helm_release.homework.metadata.app_version
}

output "image_tag" {
  value = var.image_tag
}

output "helm_chart_version" {
  value = helm_release.homework.metadata.version
}