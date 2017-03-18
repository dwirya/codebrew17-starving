angular.module('reconnectApp', [])
  .controller('MainController', ['$scope', function($scope) {
    $scope.messages = [
      {
        text:'Hello there',
        user:
          {
            nickname:'Nerdy Cat',
            avatar:'avatar/cat.png'
          }
      }, {
        text:'What do you think about the movive "moonlight" ?',
        user:
          {
            nickname:'Nerdy Cat',
            avatar:'avatar/cat.png'
          }
      }];

    $scope.sendMessage = function() {
      if ($scope.inputText) {
        $scope.messages.push({text:$scope.inputText, user:{nickname:'Me', avatar:'avatar/penguin.png'}});
        $scope.inputText = '';
      }
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
  }]);
