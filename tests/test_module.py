import json
from base64 import b64decode
from os import path as osp
from pprint import pprint
from textwrap import dedent

import pytest
from infrahouse_toolkit.terraform import terraform_apply
from mimeparse import parse_mime_type
from yaml import load, Loader

from tests.conftest import (
    LOG,
    TRACE_TERRAFORM,
    DESTROY_AFTER,
)


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
def test_module(tags, overrides, expected_result):
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
        destroy_after=DESTROY_AFTER,
        json_output=True,
        enable_trace=TRACE_TERRAFORM,
    ) as tf_output:
        print(tf_output)
        assert tf_output["result"]["value"] == expected_result
