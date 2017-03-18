angular.module('todoApp', [])
  .controller('TodoListController', function() {
    var todoList = this;
    todoList.todos = [
      {
        text:'Hello there',
        user:
          {
            nickname:'DancingCat',
            avatar:'avatar/cat.png'
          }
      }, {
        text:'What do you think about the movive "moonlight" ?',
        user:
          {
            nickname:'DancingCat',
            avatar:'avatar/cat.png'
          }
      }];

    todoList.addTodo = function() {
      todoList.todos.push({text:todoList.todoText, user:{nickname:'Me', avatar:'avatar/penguin.png'}});
      todoList.todoText = '';
    };

    // todoList.remaining = function() {
    //   var count = 0;
    //   angular.forEach(todoList.todos, function(todo) {
    //     count += todo.done ? 0 : 1;
    //   });
    //   return count;
    // };
    //
    // todoList.archive = function() {
    //   var oldTodos = todoList.todos;
    //   todoList.todos = [];
    //   angular.forEach(oldTodos, function(todo) {
    //     if (!todo.done) todoList.todos.push(todo);
    //   });
    // };
  });
