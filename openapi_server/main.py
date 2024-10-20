# coding: utf-8

"""
    MiC4.0 Element API Cluster special foundation

    MIC4.0 - Cluster Special foundations - Element-Interfaces definition

    The version of the OpenAPI document: 3.0.0 // 10.06.2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from fastapi import FastAPI

from openapi_server.apis.elements_api import router as ElementsApiRouter

app = FastAPI(
    title="MiC4.0 Element API Cluster special foundation",
    description="MIC4.0 - Cluster Special foundations - Element-Interfaces definition",
    version="3.0.0 // 10.06.2024",
)

app.include_router(ElementsApiRouter)
