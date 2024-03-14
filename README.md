# terraform-aws-tags-override
## Usage
Module will override tags.
```hcl
module "tags-override" {
  source    = "registry.infrahouse.com/infrahouse/tags-override/aws"
  version   = "~> 0.1"
  tags      = [
    {
      "name": "foo",
      "value": "bar"
    },
    {
      "name": "abc",
      "value": "def"
    }
  ]
  overrides = [
    {
      "name": "foo",
      "value": "xyz"
    }
  ]
}
```
The module above will return in the `result` output:
```hcl
[
  {
    "name": "abc", 
    "value": "def"
  },
  {
    "name": "foo", 
    "value": "xyz"
  }
]
```
Duplicate keys are removed, and the maps are sorted by the `name` value.
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | ~> 1.5 |

## Providers

No providers.

## Modules

No modules.

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_overrides"></a> [overrides](#input\_overrides) | List of tags to override var.tags | <pre>list(<br>    object(<br>      {<br>        name : string<br>        value : string<br>      }<br>    )<br>  )</pre> | `[]` | no |
| <a name="input_tags"></a> [tags](#input\_tags) | List of tags as Docker container expects | <pre>list(<br>    object(<br>      {<br>        name : string<br>        value : string<br>      }<br>    )<br>  )</pre> | `[]` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_result"></a> [result](#output\_result) | List of tags taking into account overrides |
