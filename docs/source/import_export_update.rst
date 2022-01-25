Import, Export, Update
======================

The Import / Export / Update tool lets you perform some batch actions in Janeway. You can import and export article metadata and files, and you can update some fields of existing articles.

Importing
---------
With this tool, you can create new articles in Janeway and load them directly into the desired workflow stage (peer review, copyediting, typesetting, or prepublication).

1. Download a copy of the :download:`metadata template <_static/metadata_template.csv>` and open it up to edit it. You can use most spreadsheet applications, but make sure you will be able to save it as a CSV with UTF-8 character encoding. [#]_

2. Enter the metadata, one article per row. See the `Metadata Field Reference`_ and the :download:`sample import <_static/sample_import.csv>` for pointers. For multi-author articles, insert a new row for each author, and only fill in the author fields on extra rows.

3. Save the file with a name of your choosing.

4. From the journal's dashboard, navigate to **All Articles** under **Staff** in the lower left. You need to have 'staff' access to view this page.

5. Select **Upload Update** and upload your file. (It says 'update', but this is how you import new things too.)

6. A table should load in your browser showing you the data you uploaded, before you import it. If everything looks good, select **Import**.

Exporting
---------

You can export a CSV containing metadata for all the articles currently in a given workflow stage. It will also download selected files from that stage.

1. From the journal's dashboard, navigate to All Articles under Staff in the lower left. You need to have 'staff' access to view this page.

2. Use the **Filter by Stage** drop-down menu to choose a set of articles you want to export.

3. If you want to download associated files, use the Files column to add files for each article.

4. Select **Export Articles**. A zip file should be downloaded containing the metadata in ``article_data.csv`` and the article files in subfolders numbered by article ID.


Updating
--------

You can update metadata for batches of articles in Janeway, so you don't have to click through each individual article to make the change.

1. To update one field, you have to provide data for all the fields, or at least most of them. So we recommend you first export the set of articles you want to update. See `Exporting`_.

2. Extract the zip file you exported and open the CSV in your spreadsheet software of choice (but be careful with character encoding).

3. Edit the metadata as desired. You an rearrange the columns but the column names have to stay exactly the same. See the :download:`sample update <_static/sample_update.csv>`, which shows changes made to the data in :download:`sample import <_static/sample_import.csv>`. See also the `Metadata Field Reference`_ for details on each field.

4. Save the CSV file with a name of your choosing.

5. On the **All Articles** page, select **Upload Update** and upload your CSV file.

6. A table should load in your browser showing you the data you uploaded, before you import it. If everything looks good, select **Import**.


Metadata Field Reference
------------------------

The table below shows you what actions (i.e. import, export, update) you can perform with each field (yes/no). For example, you can't *import* article IDs, because Janeway assigns them for you to make sure they're unique. But you can (must) use article IDs during the update process, so Janeway can recognize the articles.

Much the same, while you can put something in Stage to send the content to the right part of Janeway on initial import, you can't subsequently *update* the workflow stage for articles already in the system, because it might break editor or author tasks in progress.

The table also shows which fields you have to provide during imports and updates, regardless of whether you are changing those fields. For example, when you're importing new articles, you have to provide article titles. You also have to provide article titles when you are updating articles, even if you're not updating the titles but something else, like the keywords.

========================= =================================== ================= ================= =====================================
Field                     Notes                               Import            Export            Update
========================= =================================== ================= ================= =====================================
Article title             include subtitle [#]_               yes, required     yes               yes, required
Article abstract          use HTML tags for italics           yes, optional     yes               yes, optional, saves empty values
Keywords                  separate keywords with commas       yes, optional     yes               yes, optional, saves empty values
Licence                   name of licence [#]_                yes, optional     yes               yes, optional, saves empty values
Language                  plain name of language [#]_         yes, optional     yes               yes, optional, saves empty values
Author Salutation         useful in templated emails          yes, optional     yes               no, ignored
Author given name         a.k.a. first name                   yes, optional     yes               yes, optional, saves empty values
Author middle name        or middle initial                   yes, optional     yes               yes, optional, saves empty values
Author surname            a.k.a. last name                    yes, required     yes               yes, optional, saves empty values [#]_
Author email              recommended [#]_                    yes, optional     yes               complicated! [#]_
Author ORCID              starting with 'https' or the number yes, optional     yes               yes, optional, saves empty values
Author institution        _                                   yes, optional     yes               yes, optional, saves empty values
Author department         _                                   yes, optional     yes               yes, optional, saves empty values
Author biography          _                                   yes, optional     yes               yes, optional, saves empty values
Author is primary (Y/N)   Y or N [#]_                         yes, required     yes               yes, required
Author is corporate (Y/N) i.e. an organization                yes, optional     yes               no, will make duplicates
Article ID                controlled by Janeway               no, will break    yes               yes, required
DOI                       starting with '10'                  yes, optional     yes               yes, optional, ignores empty values
DOI (URL form)            starting with 'https'               no, ignored       yes               no, ignored
Date accepted             YYYY-MM-DD (or any ISO 8601 [#]_)   yes, optional     no                yes, optional, saves empty values
Date published            YYYY-MM-DD (or any ISO 8601)        yes, optional     no                yes, optional, saves empty values
Article section           e.g. 'Article', 'Review'            yes, optional     yes               yes, optional, ignores empty values
Stage                     the production workflow stage [#]_  yes, optional     yes               no, ignored [#]_
File import identifier    for advanced users [#]_             yes, optional     yes               yes, optional
Journal Code              must match Janeway                  yes, required     yes               yes, required
Journal title             must match Janeway                  yes, required     yes               yes, required
ISSN                      '0000-0000' for new journals        no, ignored       yes               no, ignored
Volume number             '0' if not specified                yes, optional     yes               no, ignored
Issue number              '0' if not specified                yes, optional     yes               no, ignored
Issue name                e.g. 'Winter 2022'                  yes, optional     yes               yes, optional, saves empty values
Issue pub date            YYYY-MM-DD (or any ISO 8601)        yes, required     yes               yes, required
========================= =================================== ================= ================= =====================================

.. [#] Using a character encoding other than UTF-8 can cause bugs during imports or updates. (`What is character encoding?`_). These apps save CSVs with UTF-8 by default: OpenRefine, LibreOffice, Google Sheets, and Apple Numbers. However! If you use Microsoft Excel, keep in mind some versions don't automatically create CSV files with UTF-8 character encoding. This may cause punctuation and special characters to be garbled on import. So, when saving, look for the 'CSV (UTF-8)' option in the drop-down box.
.. [#] Janeway doesn't yet support italics inside article titles. If your article title contains the title of a work, please use quotation marks.
.. [#] Support for licence URLs will be added in future.
.. [#] We will add support for ISO language codes in the future.
.. [#] For author names, emails, institutions, and ORCIDs, updating the values will only update what is called the 'frozen author' record for this article--that is, the author's information at the time of article submission. This information is separate from information tied to that person's Janeway account.
.. [#] Email addresses are highly recommended for correspondence authors, since many parts of the workflow involve sending emails to authors, and these won't work without email addresses.
.. [#] You should include existing email addresses in your CSV when you're trying to update other fields. You can also add or remove author records from an article with this tool. However, you shouldn't use this tool to change an author's email address, because Janeway will think you're trying to add a new author and will create a duplicate account with the new address. We will improve this behaviour in the future.
.. [#] 'Author is primary' tells Janeway which author is the correspondence author. One author must be marked 'Y' and the rest 'N'.
.. [#] See `ISO 8601 on Wikipedia`_. Examples of accepted date or date-and-time combinations: ``2022-01-04``, ``2022-01-04T10:12``, ``2022-01-04T10:12:38-05:00``.
.. [#] The workflow stage has to match one of these values exactly: ``Review``, ``Editor Copyediting``, ``typesetting_plugin``, ``pre_publication``. Otherwise the article will be put in the ``Unassigned`` stage
.. [#] Currently the workflow stage cannot be changed en masse once the articles are imported, since that might break tasks in progress. In the future we want to make it possible to change the stage of multiple articles.
.. [#] You can import some files along with the metadata, but this part of the tool is not well tested or documented. Contact Janeway support for help.

.. _`ISO 8601 on Wikipedia`: https://en.wikipedia.org/wiki/ISO_8601
.. _`What is character encoding?`: https://www.w3.org/International/questions/qa-what-is-encoding
.. _`on Windows`: https://support.microsoft.com/en-us/windows/zip-and-unzip-files-8d28fa72-f2f9-712f-67df-f80cf89fd4e5
.. _`on a Mac`: https://support.apple.com/en-gb/guide/mac-help/mchlp2528/mac