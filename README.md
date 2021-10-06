# Memento 

#### Video Demo:  <URL HERE>
#### My project will be a journaling app. It will be distinguished by its simplicity as long as it seeks that the user concentrates only on writing.

TODO
1. Create basic structure of the presentation logic
   - Landing page / Login page
   - Register Page  
   - Dashboard Page
2. Design dashboard (remembrance of simplenote, medium, write.as, telegra.ph)
   - HTML, CSS, Javascript ('interactive' buttons, etc.)
   2.1. Working with Tiny editor
      - See how to get content
      - I have two text html-element: 
         A. Title
         B. Body
         I need to get both of the text and store them into the database.
   
   2.2. EDIT MODE
      Edit-mode will be activated when user add a new entry or when user edit an old entry.
      If edit-mode is activated, in journal list (left-side-panel) will be shown only 
      the entry the user is working on.
   
   2.3. VIEW MODE
      If there is content in db, 'view mode' will be activated:
      - Show list of styled entries:
         - In order to do that I have to:
            A. Create a JS function that request via AJAX the DB-entries
            B. Create a Server-Side function that 'serialize' the Flask-SQLAlchemy response.
               I would need a serializer-extension for that. Some options:
                 - SQLAlchemy-serializer
                 - Flask-Marshmallow
               --> Let's try Flask-Marshmallow
                  - When querying the Flask-SQLAlchemy model-tables, the response I will receive from the db.Model via
                    its 'query' attribute will be a SQLAlchemy 'Query' object. I will have to somehow serialize that 
                    response in order to return a data that can be worked on JavaScript: JSON. 
                  - .dumps() with xhr.responseText returns an empty list
         - First entry from db will be shown as "selected-item"
            -  Show 'edit', 'add entry' and 'delete' buttons
            - 'Selected-item' will be shown right as editable or removable
         - If 'edit' is selected, 'edit mode' will be activated
            - Show 'save' button
         - If 'delete' is selected:
            - Delete 'Selected-item'
         - If 'add entry' is selected:
            - Add entry
   2.4. If there isn't content in db, add-entry mode will be activated
   2.5. The log-out function will log out user and delete all activity (account and entries)

3. Deploy
