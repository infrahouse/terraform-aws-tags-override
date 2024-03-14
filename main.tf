locals {
  tags_map = {
    for t in var.tags : t["name"] => t["value"]
  }
  overrides_map = {
    for t in var.overrides : t["name"] => t["value"]
  }
  result = [
    for k, v in merge(local.tags_map, local.overrides_map) : {
      name : k
      value : v
    }
  ]
  result_map = {
    for t in local.result : t["name"] => t["value"]
  }
  result_sorted = [
    for k in keys(local.result_map) : {
      name : k
      value : local.result_map[k]
    }
  ]
}
