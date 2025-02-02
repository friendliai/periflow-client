# Copyright (c) 2022-present, FriendliAI Inc. All rights reserved.

from __future__ import annotations

import uuid
from unittest.mock import patch

import pytest
import requests_mock

import friendli
from friendli.di.injector import get_injector
from friendli.utils.url import URLProvider


@pytest.fixture
def patch_safe_request(requests_mock: requests_mock.Mocker):
    friendli.token = "fake-api-key"
    injector = get_injector()
    url_provider = injector.get(URLProvider)
    requests_mock.post(url_provider.get_web_backend_uri("/api/auth/cli/refresh_token"))


@pytest.fixture
def user_project_group_context():
    with (
        patch(
            "friendli.client.base.UserRequestMixin.get_current_user_id",
            return_value=uuid.UUID("22222222-2222-2222-2222-222222222222"),
        ),
        patch(
            "friendli.client.base.get_current_group_id",
            return_value=uuid.UUID("00000000-0000-0000-0000-000000000000"),
        ),
        patch(
            "friendli.client.base.get_current_project_id",
            return_value=uuid.UUID("11111111-1111-1111-1111-111111111111"),
        ),
    ):
        yield
