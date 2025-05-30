"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)


DEFINITION = """
query QuayMembership {
  permissions: permissions_v1 {
    service
    ...on PermissionQuayOrgTeam_v1 {
      quayOrg {
        name
        instance {
          name
        }
      }
      team
      roles {
        users {
          quay_username
        }
        bots {
          quay_username
        }
        external_users {
          quay_username
        }
        expirationDate
      }
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class PermissionV1(ConfiguredBaseModel):
    service: str = Field(..., alias="service")


class QuayInstanceV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class QuayOrgV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    instance: QuayInstanceV1 = Field(..., alias="instance")


class UserV1(ConfiguredBaseModel):
    quay_username: Optional[str] = Field(..., alias="quay_username")


class BotV1(ConfiguredBaseModel):
    quay_username: Optional[str] = Field(..., alias="quay_username")


class ExternalUserV1(ConfiguredBaseModel):
    quay_username: Optional[str] = Field(..., alias="quay_username")


class RoleV1(ConfiguredBaseModel):
    users: list[UserV1] = Field(..., alias="users")
    bots: list[BotV1] = Field(..., alias="bots")
    external_users: list[ExternalUserV1] = Field(..., alias="external_users")
    expiration_date: Optional[str] = Field(..., alias="expirationDate")


class PermissionQuayOrgTeamV1(PermissionV1):
    quay_org: QuayOrgV1 = Field(..., alias="quayOrg")
    team: str = Field(..., alias="team")
    roles: list[RoleV1] = Field(..., alias="roles")


class QuayMembershipQueryData(ConfiguredBaseModel):
    permissions: list[Union[PermissionQuayOrgTeamV1, PermissionV1]] = Field(..., alias="permissions")


def query(query_func: Callable, **kwargs: Any) -> QuayMembershipQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        QuayMembershipQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return QuayMembershipQueryData(**raw_data)
