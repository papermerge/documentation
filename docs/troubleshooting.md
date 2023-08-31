# Troubleshooting

## Gray Screen


It may happen that you open |project| in web browser you will see just gray
screen instead
of meaningful UI.

One workaround for this is to delete cookies for respective domain.

Here is how:

![](../img/troubleshooting/delete-cookies.gif)

## The fields parent, title must make a unique set

If you import document twice to same target location, you will get a not
very friendly error which says something about "The fields parent, title
must make a unique set.", it means that you cannot have two documents with
same title in one folder, to put it in other words "You already have document
with same title in target folder":

![](../troubleshooting/error-when-importing-document.svg)

In order to avoid that issue, either rename your local document (source),
or rename the document on the server (target).

Another way you can avoid that weird error is to use `--delete` flag
as described in `import_folders`
