# Path Templates

Imagine you've got couple of receipts from your customer in the inbox.
They are in your inbox. But inbox is just temporary location, so you'll need to move
documents to their "final destination" - target folder.

Or may you just want to upload couple of documents yourself. Still you need to decide
where to place them.

Regardless which way documents end up in {{ extra.project }} - every time you need
to decide where you place them: which folder?


## Target Folder

The question "what is the target folder for document X" may not seem like a big deal.
And indeed - if you just do it for very first folder, only one time it is simple.
But more your document base grows, more complex folder layout you have more vexed
the question becomes. Especially if you do it say, onece a week.

More realistic scenario would be this: you work on your lovely project,
you are fully focused on your project. You receive an invoice from your customer
(we will refer to this customer - Coco). Now you decide to upload Coco's invoice
into {{ extra.project }}.

And... where should you place it?
Is it in `/home/Customers/2024/coco/invoice-2024-01.pdf`?
Or in `/home/Invoices/2024/Customers/coco-2024-01.pdf`?
Or maybe in `/home/My Documents/invoices`?

You see, we humans tend to forget. The question of the target folder is vexed
one. It distracts you from your real tasks.

## Path Templates

Meet *path templates*. The idea is simple: you need to decide where to place
your receipts only once. Once you decide where you put to them - you write it
down as "path template" and then all your receipts will automatically be
placed to that path. Of course you can do that for any document type.

Basically, for each document type you create a "template" of
the place where documents of that type will be stored. And then {{extra.project}}
will use that information to move the document to the
target folder automatically :magic_wand:!


!!! Info

	Path templates are per document type. They create a "template"
	of where documents of that type will be placed. The path includes
	both target folder and file name.

Let's see couple of examples.

