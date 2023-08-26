.. _automation:


Automates
============

Automates are very handy  if you want to apply automatically certain actions
on incoming documents. For example, if document contains specific keywords
(like groceries store name) then automatically add tag "groceries" on it. Even
better use case would be: if document contains specific keywords apply
"groceries" tag on the document AND move it from *Inbox* to
:menuselection:`Expenses --> Groceries` folder. Incoming documents are those
found in your *Inbox* folder.

If you want to see automates in action watch following screencast. The rest of
this chapter explains automate feature in detail.

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/5adbHHmNcEw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


With Automation feature you can automate repetitive tasks like:

1. moving documents into their destination folder
2. assigning specific tags to the document


.. figure:: ../img/user-manual/automates/01-automates-v2.png
  :alt: List of document automate instances

  Figure 1 - Example of automate instance

Each automate instance consists of:

* name or a title - give it whatever name you like    
* keywords - terms or words to look up in the document to figure out if current automate is applicable for given document
* :ref:`matching algorithm <document_matching_alg>` - method used to decide if document matches the automate 
* :ref:`case sensitivity attribute <case_sensitivity_attr>` - are keywords specified in match case sensitive?
* (optional) destination folder - where shall it move the matched document? 
* (optional) tags - which tags shall it associate to the matched document?

Note that last two attributes of Automates - destination folder and tags - are
optional. You may indicate one of them, both or neither.

.. _document_matching_alg:

Document Matching Algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to decide if automate instance applies to current document - it will look for certain
keywords in the document. For example if document contains capital case REWE, then this document
must be routed to folder Expenses/Groceries; if document contains word Deutschlandradio (german word which translates to english as German radio), then it will be routed to
ARD ZDF Briefe

.. caution::
  
   It is crucial to understand that **matching is per Page**. Thus, statement *match a document* is not entirely correct. 
   Automation processes is triggered every time when :ref:`OCR <ocr>` for
   certain page completes. :ref:`OCRed <ocrs>` page is sent to automation module and
   Papermerge will try to match each automate instance on it. In case there is
   a match - it is considered that document matched automate criteria,
   although technically correct is - page of respective the document matched!

There are four different ways to perform a match:

1. Any
2. All
3. Literal
4. Regular Expression

With ``Any`` matching algorithm, document matches **if any of mentioned
keyword will match**. With ``All``, document matches **if all mentioned
keywords are found in document**. Keywords order does not matter.
With ``Literal`` matching algorithm, text you enter must appear in the
document exactly as you've entered it.
You can use ``Regular Expression`` for matching criteria. Regular expressions
is a general programming method of text matching. Computer programmers usually
know what it means.

Matching keywords should be separated by one or more spaces.

.. figure:: ../img/user-manual/automates/document-matching-keywords-delimited-by-space-v2.png
  :alt: Keywords for matching criteria separated by one or more space characters

  Figure 2 - Keywords must be separated by one or more space characters

.. _case_sensitivity_attr:

Case Sensitivity Attribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If case sensitivity attribute is checked, the matching algorithms will look up for
words occurrences with **exact same letter case as matching keywords**

For example if "schnell" is mentioned as keyword and *Is case sensitive* is
checked then occurrences in the document of terms "SCHNELL", "Schnell",
"schneLL" will be ignored because of mismatched letter case i.e. document will
not match automate criteria.

On the other hand, if very same keyword "schnell" is used but *Is case
sensitive* attributed is unchecked, then any of following terms "SCHNELL",
"Schnell", "schneLL" will match i.e. document will match automate criteria.


Inbox + Automates
~~~~~~~~~~~~~~~~~~~

Automates run only for documents in ``Inbox`` folder.

Imported documents from :ref:`local watch directory <importer_directory>` or
:ref:`from email account <importer_imap>` end up in your ``Inbox`` folder.
Papermerge will apply automates only on the documents in ``Inbox`` -
regardless where those documents were imported from. The side effect of this
feature is that **automates will run on documents in** ``Inbox`` **even if you
uploaded them manually** - this one is a very useful trick to test your
automates.


.. note::

    There is a good reason why automates apply only on the documents from
    ``Inbox``. The reason is that in ``Inbox`` documents may disappear. In
    other words -  it is acceptable for documents to suddenly move from
    ``Inbox`` to another folder - due to automation match. 
    If automates would be applied on any folder - then imagine
    how confused you might be if documents would unexpectedly disappear from
    your current folder (due to automation match)!


Automates and UI Logs
~~~~~~~~~~~~~~~~~~~~~~

You can check which automate matched specific document by looking at UI Logs:


.. figure:: ../img/user-manual/automates/02-ui-logs-v2.png

  Figure 3

In UI Log entry you can see document's name, page number and document id on which
Automates were applied (remember, automates are applied per Page!). 
Also, you can see that text which was extracted from that document:

.. note::

  UI Logs are very convient to see the **extracted text** from the document.
  Depending on the quality of the scan, extracted text may or may not exactly match
  textual content of the document. For instance in figure below, OCR engine extracted text
  "SCHNEIL" although the actual text on the receipt was "SCHNELL". Use UI Logs to spot such errors
  and adjust *MATCH* term.

.. figure:: ../img/user-manual/automates/03-ui-logs-v2.png

  Figure 4

In order to check which Automate matched this document/page, you need to **scroll to the
very bottom of the message**:

.. figure:: ../img/user-manual/automates/04-ui-logs-v2.png

  Figure 5


Troubleshooting Mismatched Automates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writing Automates involves little bit of guesswork. Even if you know for sure
that certain words will occur in the document, it will take couple of trial
and error cycles until you'll end up with correct ``match`` field.

To support this try-error cycle, with Papermerge you can manually trigger
automates. It is very intuitive how re-run automates:

1. Select Automate you wish to run
2. Select ``Run selected automates`` in the action drop down on the right
3. Click ``Apply`` button

.. figure:: ../img/user-manual/automates/manually-run-automates-v2.png
  :alt: Manually run selected automates

  Figure 6 - Manually run selected automates

Let's consider an example which will illustrate how Automates are
troubleshooted. The goal is to create an Automate which will automatically
move Schnell receipts to :menuselection:`Expenses --> Groceries` folder and
will tag them with ``groceries``, ``receipt``, ``schnell`` tags.
For this purpose, following Automate was created:

.. figure:: ../img/user-manual/automates/automate-and-two-receipts.png

  Figure 7

Notice that ``Match`` field has as value one single lowercase keyword "schnell". ``Is case sensitive`` field is checked.

For the beginning, two receipts shown in Figure 7 are uploaded to ``Inbox`` folder.

.. note::

  Automates are triggered for all :ref:`incoming documents
  <incoming_documents>`, even if they are manually uploaded to ``Inbox``
  folder. However, if you cut/paste document(s) from other folder to ``Inbox``
  - automates **won't run**.

To make sure that automates ran, check last entries in ``UI Logs``. Also, in
``UI Logs`` you will see actual extracted text the automates were compared
with. For Automate and receipts from Figure 7 - uploaded receipts still will
be in ``Inbox``. The reason of that, is checked ``Is case sensitive``
attribute: in extracted text for "schnell" all uppercase while our keyword is
all lowercase.

Let's try again. Use following steps:

1. Uncheck ``Is case sensitive attribute``
2. Save changes *schnell receipts* automate
3. Select *schnell receipts* automate
4. run Automate again using action drop down menu :menuselection:`Action --> Run selected automates --> Apply`


You will notice that one of the two receipts moved indeed from ``Inbox`` folder to "Groceries" folder. Also it has applied all three tags as depicted in Figure 8.

.. figure:: ../img/user-manual/automates/troubleshooting-automates-step-2.png
  :scale: 80%

  Figure 8 - after unchecking `Is case sensitive` attribute and running again Automate one of the two receipts was indeed moved from ``Inbox`` to :menuselection:`Expenses --> Groceries` folder and has all three tags applied.

Why other receipt didn't match ? Let's have a closer look the UI Logs. Open last UI Log entry which starts with *Running automates for document brother_004026.pdf* text:

.. figure:: ../img/user-manual/automates/ocr-engine-made-a-mistake.png
  
  Figure 9 - OCR engine got confused and extracted "SCHNEIL" instead of "SCHNELL"

You see in Figure 9 above that OCR engine got confused and extracted slightly wrong text. To take into account this error as well, add to ``Match`` field of Automate "schneil" keyword as well:

.. figure:: ../img/user-manual/automates/automate-with-two-keywords.png

  Figure 10


Notice that ``Matching Algorithm`` is ``Any``, this means that Automate will
match if any mentioned keywords will match. After saving and
rerunning automate - second receipt is successfully moved to Groceries folder
and it has all three tags applied as you can see in picture below:

.. figure:: ../img/user-manual/automates/correctly-applied-automates.png

  Figure 11 - After two attempts finally Automate matched receipts and they were moved
  into target folder.

Watch following screencast to see this troubleshooting use case in action:

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/825woFE5Cas" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
