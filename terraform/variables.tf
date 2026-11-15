variable "namespace" {
  type    = string
  default = "production"
}

variable "environment" {
  type    = string
  default = "prod"
}

variable "image_tag" {
  type    = string
  default = "1.0.0"
}