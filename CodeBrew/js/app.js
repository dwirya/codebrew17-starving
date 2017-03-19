angular.module('reconnectApp', [])
.controller('MainController', ['$scope', function($scope) {
    $scope.connected = false;
    $scope.questions = ["For a person you loved deeply, would you be willing to move to a distant country with little chance of seeing your friends and family again?",
"If you were to die this evening with no opportunity to communicate with anyone, what would you most regret not having told someone? Why haven't you told them?",
"Would you spend the next 10 years of happiness with the love of and then witness them pass away before spending the rest of your life alone or spend the rest of your life alone from the very beginning?",
"If a new medicine were developed that would cure cancer but would cause a fatal reaction in 10 percent of the people who took it, would you want it released?",
"If you had to spend one day in any era of history, which era would it be?",
"If you could travel back 100 years back in time and only bring one item with you, what would it be?",
"Would you rather to be extremely successful professionally and have a tolerable yet unexciting private life or have an extremely happy life but a very uninspiring and unhappy professional life?",
"If you could choose your child's personality at birth, would you?",
"Would you be willing imprison an innocent child for their whole life if it would end all suffering and sadness in the rest of the world - effectively producing a Utopian world?"];
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

    $scope.timeModal = function() {
      var time = 10,
          display = document.querySelector('#time');
      startTimer(time, display);

    }

    function startTimer(duration, display) {
        var timer = duration, minutes, seconds;
        setInterval(function () {
            minutes = parseInt(timer / 60, 10);
            seconds = parseInt(timer % 60, 10);

            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;

            display.textContent = minutes + ":" + seconds;

            if (timer <= 0) {
                $('#options').modal('show');
            } else {
              timer -= 1;
            }
        }, 1000);
    }

  }]);
