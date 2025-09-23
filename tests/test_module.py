import json
from os import path as osp
from textwrap import dedent

import pytest
from pytest_infrahouse import terraform_apply


@pytest.mark.parametrize(
    "tags, overrides, expected_result",
    [
        ([], [], []),
        ([{"name": "foo", "value": "bar"}], [], [{"name": "foo", "value": "bar"}]),
        (
            [{"name": "foo", "value": "bar"}],
            [{"name": "foo", "value": "xyz"}],
            [{"name": "foo", "value": "xyz"}],
        ),
        (
            [{"name": "foo", "value": "bar"}, {"name": "abc", "value": "def"}],
            [{"name": "foo", "value": "xyz"}],
            [{"name": "abc", "value": "def"}, {"name": "foo", "value": "xyz"}],
        ),
    ],
)
def test_module(tags, overrides, expected_result, keep_after):
    terraform_dir = "test_data"
    module_dir = osp.join(terraform_dir, "test_module")

    with open(osp.join(module_dir, "terraform.tfvars"), "w") as fp:
        fp.write(
            dedent(
                f"""
                tags = {json.dumps(tags)}
                overrides = {json.dumps(overrides)}
                """
            )
        )

    with terraform_apply(
        module_dir,
        destroy_after=not keep_after,
        json_output=True,
    ) as tf_output:
        print(tf_output)
        assert tf_output["result"]["value"] == expected_result
