from abc import ABC, abstractmethod

class EditorState(ABC):

    @abstractmethod
    def edit(self, editor):
        pass

    @abstractmethod
    def save(self, editor):
        pass

    @abstractmethod
    def print(self, editor):
        pass

class EditingState(EditorState):
    
    def edit(self, editor):
        # Simulate editing behavior
        print("Editing the document")
        editor.set_content("This is the edited content")

    def save(self, editor):
        # Save the edited content to a file
        print("Saving changes to a file")
        editor.set_state(editor.get_viewing_state())  # Transition to ViewingState

    def print(self, editor):
        # Print the edited content
        print("Printing the edited content")
        editor.set_state(editor.get_printing_state())  # Transition to PrintingState

class PrintingState(EditorState):
    
    def edit(self, editor):
        # Editing is not allowed during printing
        print("Cannot edit while printing")
        editor.set_state(editor.get_editing_state())  # Transition to EditingState

    def save(self, editor):
        # Saving is not allowed during printing
        print("Cannot save while printing")
        editor.set_state(editor.get_viewing_state())  # Transition to ViewingState

    def print(self, editor):
        # Print the content
        print("Printing the content")
        editor.set_state(editor.get_viewing_state())  # Transition to ViewingState

class ViewingState(EditorState):
    
    def edit(self, editor):
        # Editing is not allowed in viewing mode
        print("Cannot edit in viewing mode")
        editor.set_state(editor.get_editing_state())  # Transition to EditingState

    def save(self, editor):
        # Saving is not allowed in viewing mode
        print("Cannot save in viewing mode")
        editor.set_state(editor.get_editing_state())  # Transition to EditingState

    def print(self, editor):
        # Print the content
        print("Printing the content")
        editor.set_state(editor.get_printing_state())  # Transition to PrintingState

class DocumentEditor:

    def __init__(self, action):
        self._editing_state = EditingState()
        self._printing_state = PrintingState()
        self._viewing_state = ViewingState()
        self._content = "Initial content"
        self._current_state = None

        if action == 'viewing':
            self._current_state = self._viewing_state
        elif action == 'printing':
            self._current_state = self._printing_state
        else:
            self._current_state = self._editing_state

    def edit(self):
        self._current_state.edit(self)

    def save(self):
        self._current_state.save(self)

    def print(self):
        self._current_state.print(self)

    def set_state(self, state: EditorState):
        self._current_state = state

    def get_editing_state(self):
        return self._editing_state
    
    def get_viewing_state(self):
        return self._viewing_state
    
    def get_printing_state(self):
        return self._printing_state

    def set_content(self, content):
        self._content = content

    def get_content(self):
        return self._content

if __name__ == '__main__':
    # Example usage
    editor = DocumentEditor('editing')
    editor.edit()  # Simulate editing the document
    editor.save()  # Simulate saving the edited content to a file
    editor.print()  # Simulate printing the edited content

   
