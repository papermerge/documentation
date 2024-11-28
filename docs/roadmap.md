# Roadmap 2025

For year 2025 we plan to implement in {{ extra.project }} following major features:

1. Localization
2. UI Settings
3. Per object access management
4. Group Ownership
5. Search by Custom Fields
6. System Audit


## 1. Localization

Localization is about making UI available in other languages than English.
On initial release application will be available in English and German languages.
It will be up to community to provides translation for other languages.


## 2. UI Settings

Currently, the only way to configure {{extra.project}} is via environment
variables. UI Settings means - users will be able to change configurations
like default UI language, dark/light UI mode, default language to use in OCR,
date format etc via web user interface.


## 3. Per Object Access Management

This is big one. "Per Object" here means access management for specific folder or documents.
In short, it is about shared folders and shared documents.
We will address sharing of tags, categories, and custom fields.

## 4. Group Ownership

It is not clear yet if this one will be shipped as separate release or
together with 3. In any case, this feature is about adding group ownership for
the objects (related to 3.) Current version (3.3) supports only ownership of
resources like folders, documents, tags, custom fields, categories by
individual user (the user who created the resource). The feature is about
adding one extra possibility of resource (folder, document, tag etc) being
owned by a group of individuals.

## 5. Search by Custom Fields

The title says it all.

## 6. System Audit

Here System = {{ extra.project }}. The feature is about providing insights what happens
in the system i.e. who did what and when.
