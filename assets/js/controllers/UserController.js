/**
 * Created by abelyaev on 30.10.15.
 */
app.controller('UserController', function ($scope, user_info){
  user_info.list(function(user_info) {
    $scope.user_info = user_info;
  });
});