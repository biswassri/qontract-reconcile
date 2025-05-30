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

from reconcile.gql_definitions.fragments.oc_connection_cluster import OcConnectionCluster
from reconcile.gql_definitions.fragments.saas_slo_document import SLODocument
from reconcile.gql_definitions.fragments.saas_target_namespace import SaasTargetNamespace
from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


DEFINITION = """
fragment CommonJumphostFields on ClusterJumpHost_v1 {
  hostname
  knownHosts
  user
  port
  remotePort
  identity {
    ... VaultSecret
  }
}

fragment OcConnectionCluster on Cluster_v1 {
  name
  serverUrl
  internal
  insecureSkipTLSVerify
  jumpHost {
    ...CommonJumphostFields
  }
  automationToken {
    ...VaultSecret
  }
  clusterAdminAutomationToken {
    ...VaultSecret
  }
  disable {
    integrations
  }
}

fragment SLODocument on SLODocument_v1 {
    name
    namespaces {
      prometheusAccess {
         url
         username {
         ... VaultSecret
         }
         password {
           ... VaultSecret
         }
      }
      namespace {
        name
        app {
          name
        }
        cluster {
          name
          automationToken {
          ... VaultSecret
          }
          prometheusUrl
          spec {
            private
          }
        }
      }
      SLONamespace {
        name
      }
    }
    slos {
      name
      expr
      SLIType
      SLOParameters {
        window
      }
      SLOTarget
      SLOTargetUnit
    }
}

fragment SaasTargetNamespace on Namespace_v1 {
  name
  labels
  delete
  path
  environment {
    name
    labels
    parameters
    secretParameters {
      name
      secret {
        ...VaultSecret
      }
    }
  }
  app {
    name
    parentApp {
      name
    }
    labels
    selfServiceRoles {
      name
    }
    serviceOwners {
      name
      email
    }
    codeComponents {
      url
      blockedVersions
      hotfixVersions
    }
  }
  cluster {
    name
    serverUrl
    internal
    insecureSkipTLSVerify
    labels
    jumpHost {
      ...CommonJumphostFields
    }
    automationToken {
      ...VaultSecret
    }
    clusterAdminAutomationToken {
      ...VaultSecret
    }
    disable {
      integrations
    }
    spec {
      region
    }
    externalConfiguration {
      labels
    }
  }
  skupperSite {
    delete
  }
}

fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query SaasFiles {
  saas_files: saas_files_v2 {
    path
    name
    labels
    app {
      name
      parentApp {
        name
      }
      selfServiceRoles {
        name
      }
      serviceOwners {
        name
        email
      }
      codeComponents {
        url
        blockedVersions
        hotfixVersions
      }
    }
    pipelinesProvider {
      name
      provider
      ... on PipelinesProviderTekton_v1 {
        namespace {
          name
          cluster {
            ...OcConnectionCluster
            consoleUrl
          }
        }
        defaults {
          pipelineTemplates {
            openshiftSaasDeploy {
              name
            }
          }
        }
        pipelineTemplates {
          openshiftSaasDeploy {
            name
          }
        }
      }
    }
    deployResources {
      requests {
        cpu
        memory
      }
      limits {
        cpu
        memory
      }
    }
    slack {
      output
      workspace {
        name
        integrations {
          name
          token {
            ...VaultSecret
          }
          channel
          icon_emoji
          username
        }
      }
      channel
      notifications {
        start
      }
    }
    managedResourceTypes
    managedResourceNames {
      resource
      resourceNames
    }
    takeover
    deprecated
    compare
    timeout
    skipSuccessfulDeployNotifications
    publishJobLogs
    clusterAdmin
    imagePatterns
    allowedSecretParameterPaths
    use_channel_in_image_tag
    authentication {
      code {
        ...VaultSecret
      }
      image {
        ...VaultSecret
      }
    }
    parameters
    secretParameters {
      name
      secret {
        ...VaultSecret
      }
    }
    validateTargetsInApp
    validatePlannedData
    resourceTemplates {
      name
      url
      path
      provider
      hash_length
      parameters
      secretParameters {
        name
        secret {
          ...VaultSecret
        }
      }
      targets {
        path
        name
        namespace {
          ...SaasTargetNamespace
        }
        slos {
         ...SLODocument 
        }
        namespaceSelector {
          jsonPathSelectors {
            include
            exclude
          }
        }
        provider
        ref
        promotion {
          auto
          publish
          subscribe
          redeployOnPublisherConfigChange
          soakDays
          schedule
          promotion_data {
            channel
            data {
              type
              ... on ParentSaasPromotion_v1 {
                parent_saas
                target_config_hash
              }
            }
          }
        }
        parameters
        secretParameters {
          name
          secret {
            ...VaultSecret
          }
        }
        upstream {
          instance {
            name
            serverUrl
          }
          name
        }
        images {
          org {
            name
            instance {
              url
            }
          }
          name
        }
        disable
        delete
      }
    }
    selfServiceRoles {
      name
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class AppV1_AppV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class RoleV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class OwnerV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    email: str = Field(..., alias="email")


class AppCodeComponentsV1(ConfiguredBaseModel):
    url: str = Field(..., alias="url")
    blocked_versions: Optional[list[str]] = Field(..., alias="blockedVersions")
    hotfix_versions: Optional[list[str]] = Field(..., alias="hotfixVersions")


class AppV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    parent_app: Optional[AppV1_AppV1] = Field(..., alias="parentApp")
    self_service_roles: Optional[list[RoleV1]] = Field(..., alias="selfServiceRoles")
    service_owners: Optional[list[OwnerV1]] = Field(..., alias="serviceOwners")
    code_components: Optional[list[AppCodeComponentsV1]] = Field(..., alias="codeComponents")


class PipelinesProviderV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    provider: str = Field(..., alias="provider")


class ClusterV1(OcConnectionCluster):
    console_url: str = Field(..., alias="consoleUrl")


class NamespaceV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    cluster: ClusterV1 = Field(..., alias="cluster")


class PipelinesProviderTektonObjectTemplateV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class PipelinesProviderPipelineTemplatesV1(ConfiguredBaseModel):
    openshift_saas_deploy: PipelinesProviderTektonObjectTemplateV1 = Field(..., alias="openshiftSaasDeploy")


class PipelinesProviderTektonProviderDefaultsV1(ConfiguredBaseModel):
    pipeline_templates: PipelinesProviderPipelineTemplatesV1 = Field(..., alias="pipelineTemplates")


class PipelinesProviderTektonV1_PipelinesProviderPipelineTemplatesV1_PipelinesProviderTektonObjectTemplateV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class PipelinesProviderTektonV1_PipelinesProviderPipelineTemplatesV1(ConfiguredBaseModel):
    openshift_saas_deploy: PipelinesProviderTektonV1_PipelinesProviderPipelineTemplatesV1_PipelinesProviderTektonObjectTemplateV1 = Field(..., alias="openshiftSaasDeploy")


class PipelinesProviderTektonV1(PipelinesProviderV1):
    namespace: NamespaceV1 = Field(..., alias="namespace")
    defaults: PipelinesProviderTektonProviderDefaultsV1 = Field(..., alias="defaults")
    pipeline_templates: Optional[PipelinesProviderTektonV1_PipelinesProviderPipelineTemplatesV1] = Field(..., alias="pipelineTemplates")


class ResourceRequestsRequirementsV1(ConfiguredBaseModel):
    cpu: str = Field(..., alias="cpu")
    memory: str = Field(..., alias="memory")


class ResourceLimitsRequirementsV1(ConfiguredBaseModel):
    cpu: Optional[str] = Field(..., alias="cpu")
    memory: str = Field(..., alias="memory")


class DeployResourcesV1(ConfiguredBaseModel):
    requests: ResourceRequestsRequirementsV1 = Field(..., alias="requests")
    limits: ResourceLimitsRequirementsV1 = Field(..., alias="limits")


class SlackWorkspaceIntegrationV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    token: VaultSecret = Field(..., alias="token")
    channel: str = Field(..., alias="channel")
    icon_emoji: str = Field(..., alias="icon_emoji")
    username: str = Field(..., alias="username")


class SlackWorkspaceV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    integrations: Optional[list[SlackWorkspaceIntegrationV1]] = Field(..., alias="integrations")


class SlackOutputNotificationsV1(ConfiguredBaseModel):
    start: Optional[bool] = Field(..., alias="start")


class SlackOutputV1(ConfiguredBaseModel):
    output: Optional[str] = Field(..., alias="output")
    workspace: SlackWorkspaceV1 = Field(..., alias="workspace")
    channel: Optional[str] = Field(..., alias="channel")
    notifications: Optional[SlackOutputNotificationsV1] = Field(..., alias="notifications")


class ManagedResourceNamesV1(ConfiguredBaseModel):
    resource: str = Field(..., alias="resource")
    resource_names: list[str] = Field(..., alias="resourceNames")


class SaasFileAuthenticationV1(ConfiguredBaseModel):
    code: Optional[VaultSecret] = Field(..., alias="code")
    image: Optional[VaultSecret] = Field(..., alias="image")


class SaasSecretParametersV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    secret: VaultSecret = Field(..., alias="secret")


class SaasResourceTemplateV2_SaasSecretParametersV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    secret: VaultSecret = Field(..., alias="secret")


class JsonPathSelectorsV1(ConfiguredBaseModel):
    include: list[str] = Field(..., alias="include")
    exclude: Optional[list[str]] = Field(..., alias="exclude")


class SaasResourceTemplateTargetNamespaceSelectorV1(ConfiguredBaseModel):
    json_path_selectors: JsonPathSelectorsV1 = Field(..., alias="jsonPathSelectors")


class PromotionChannelDataV1(ConfiguredBaseModel):
    q_type: str = Field(..., alias="type")


class ParentSaasPromotionV1(PromotionChannelDataV1):
    parent_saas: Optional[str] = Field(..., alias="parent_saas")
    target_config_hash: Optional[str] = Field(..., alias="target_config_hash")


class PromotionDataV1(ConfiguredBaseModel):
    channel: Optional[str] = Field(..., alias="channel")
    data: Optional[list[Union[ParentSaasPromotionV1, PromotionChannelDataV1]]] = Field(..., alias="data")


class SaasResourceTemplateTargetPromotionV1(ConfiguredBaseModel):
    auto: Optional[bool] = Field(..., alias="auto")
    publish: Optional[list[str]] = Field(..., alias="publish")
    subscribe: Optional[list[str]] = Field(..., alias="subscribe")
    redeploy_on_publisher_config_change: Optional[bool] = Field(..., alias="redeployOnPublisherConfigChange")
    soak_days: Optional[int] = Field(..., alias="soakDays")
    schedule: Optional[str] = Field(..., alias="schedule")
    promotion_data: Optional[list[PromotionDataV1]] = Field(..., alias="promotion_data")


class SaasResourceTemplateTargetV2_SaasSecretParametersV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    secret: VaultSecret = Field(..., alias="secret")


class JenkinsInstanceV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    server_url: str = Field(..., alias="serverUrl")


class SaasResourceTemplateTargetUpstreamV1(ConfiguredBaseModel):
    instance: JenkinsInstanceV1 = Field(..., alias="instance")
    name: str = Field(..., alias="name")


class QuayInstanceV1(ConfiguredBaseModel):
    url: str = Field(..., alias="url")


class QuayOrgV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    instance: QuayInstanceV1 = Field(..., alias="instance")


class SaasResourceTemplateTargetImageV1(ConfiguredBaseModel):
    org: QuayOrgV1 = Field(..., alias="org")
    name: str = Field(..., alias="name")


class SaasResourceTemplateTargetV2(ConfiguredBaseModel):
    path: Optional[str] = Field(..., alias="path")
    name: Optional[str] = Field(..., alias="name")
    namespace: Optional[SaasTargetNamespace] = Field(..., alias="namespace")
    slos: Optional[list[SLODocument]] = Field(..., alias="slos")
    namespace_selector: Optional[SaasResourceTemplateTargetNamespaceSelectorV1] = Field(..., alias="namespaceSelector")
    provider: Optional[str] = Field(..., alias="provider")
    ref: str = Field(..., alias="ref")
    promotion: Optional[SaasResourceTemplateTargetPromotionV1] = Field(..., alias="promotion")
    parameters: Optional[Json] = Field(..., alias="parameters")
    secret_parameters: Optional[list[SaasResourceTemplateTargetV2_SaasSecretParametersV1]] = Field(..., alias="secretParameters")
    upstream: Optional[SaasResourceTemplateTargetUpstreamV1] = Field(..., alias="upstream")
    images: Optional[list[SaasResourceTemplateTargetImageV1]] = Field(..., alias="images")
    disable: Optional[bool] = Field(..., alias="disable")
    delete: Optional[bool] = Field(..., alias="delete")


class SaasResourceTemplateV2(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    url: str = Field(..., alias="url")
    path: str = Field(..., alias="path")
    provider: Optional[str] = Field(..., alias="provider")
    hash_length: Optional[int] = Field(..., alias="hash_length")
    parameters: Optional[Json] = Field(..., alias="parameters")
    secret_parameters: Optional[list[SaasResourceTemplateV2_SaasSecretParametersV1]] = Field(..., alias="secretParameters")
    targets: list[SaasResourceTemplateTargetV2] = Field(..., alias="targets")


class SaasFileV2_RoleV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class SaasFileV2(ConfiguredBaseModel):
    path: str = Field(..., alias="path")
    name: str = Field(..., alias="name")
    labels: Optional[Json] = Field(..., alias="labels")
    app: AppV1 = Field(..., alias="app")
    pipelines_provider: Union[PipelinesProviderTektonV1, PipelinesProviderV1] = Field(..., alias="pipelinesProvider")
    deploy_resources: Optional[DeployResourcesV1] = Field(..., alias="deployResources")
    slack: Optional[SlackOutputV1] = Field(..., alias="slack")
    managed_resource_types: list[str] = Field(..., alias="managedResourceTypes")
    managed_resource_names: Optional[list[ManagedResourceNamesV1]] = Field(..., alias="managedResourceNames")
    takeover: Optional[bool] = Field(..., alias="takeover")
    deprecated: Optional[bool] = Field(..., alias="deprecated")
    compare: Optional[bool] = Field(..., alias="compare")
    timeout: Optional[str] = Field(..., alias="timeout")
    skip_successful_deploy_notifications: Optional[bool] = Field(..., alias="skipSuccessfulDeployNotifications")
    publish_job_logs: Optional[bool] = Field(..., alias="publishJobLogs")
    cluster_admin: Optional[bool] = Field(..., alias="clusterAdmin")
    image_patterns: list[str] = Field(..., alias="imagePatterns")
    allowed_secret_parameter_paths: Optional[list[str]] = Field(..., alias="allowedSecretParameterPaths")
    use_channel_in_image_tag: Optional[bool] = Field(..., alias="use_channel_in_image_tag")
    authentication: Optional[SaasFileAuthenticationV1] = Field(..., alias="authentication")
    parameters: Optional[Json] = Field(..., alias="parameters")
    secret_parameters: Optional[list[SaasSecretParametersV1]] = Field(..., alias="secretParameters")
    validate_targets_in_app: Optional[bool] = Field(..., alias="validateTargetsInApp")
    validate_planned_data: Optional[bool] = Field(..., alias="validatePlannedData")
    resource_templates: list[SaasResourceTemplateV2] = Field(..., alias="resourceTemplates")
    self_service_roles: Optional[list[SaasFileV2_RoleV1]] = Field(..., alias="selfServiceRoles")


class SaasFilesQueryData(ConfiguredBaseModel):
    saas_files: Optional[list[SaasFileV2]] = Field(..., alias="saas_files")


def query(query_func: Callable, **kwargs: Any) -> SaasFilesQueryData:
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
        SaasFilesQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return SaasFilesQueryData(**raw_data)
