# What's new in 3.3?

Version 3.3 introduces following new major features:

- Document Types
- Custom Fields
- Path Templates
- S3 storage backend

## Document Types

Document types enable you to categorize documents. You
can define types such as "Receipt", "Invoice", or "Contract".

Read more about [document type in user manual](user/document-types.md)


## Custom Fields

New, extremely powerful, flexible and easy to use feature. Before version 2.1
custom fields were named "metadata", however, we introduced a significant
twist in the concept: instead of being assigned directly to the document,
custom fields are now assigned via document types.

Read more about [custom fields in user manual](user/custom-fields.md)


## Path Templates

You need to decide where to place the document only once.
Once decided - you never need to worry in which folder does
the document X or Y belong - it will be handled automatically.
Path templates are per document category.

Read more about it in [Path Templates](user/path-templates.md)


## S3 Storage Backend


You can configure S3 compatible storage for you documents. It means that you
may configure {{ extra.project }} to store documents on S3 storage.

Feature is there, but document is not :slightly_frowning_face:.
Documentation is on this topic is being written :hourglass: ...