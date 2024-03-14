variable "tags" {
  description = "List of tags as Docker container expects"
  type = list(
    object(
      {
        name : string
        value : string
      }
    )
  )
  default = []
}

variable "overrides" {
  description = "List of tags to override var.tags"
  type = list(
    object(
      {
        name : string
        value : string
      }
    )
  )
  default = []
}
