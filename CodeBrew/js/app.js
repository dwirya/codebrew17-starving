angular.module('reconnectApp', [])
  .controller('MainController', ['$scope', function($scope) {
    $scope.connected = false;
    $scope.messages = [
      {
        text:'Hello there',
        user:
          {
            name: 'Anushka',
            profile: 'avatar/Anushka_real.jpg',
            nickname:'Nerdy Cat',
            avatar:'avatar/cat.png'
          }
      }, {
        text:'What do you think about the movive "moonlight" ?',
        user:
          {
            name: 'Anushka',
            profile: 'avatar/Anushka_real.jpg',
            nickname:'Nerdy Cat',
            avatar:'avatar/cat.png'
          }
      }];

    $scope.sendMessage = function() {
      if ($scope.inputText) {
        $scope.messages.push({text:$scope.inputText, user:{name:'Jun', profile:'avatar/Jun_real.jpg', nickname:'Me', avatar:'avatar/penguin.png'}});
        $scope.inputText = '';
      }
    };

    $scope.clickFn = function() {
      $scope.connected = true;
      $('#real-profile').modal('show');
    }

  }]);
