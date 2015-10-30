app.factory('user_info', function($http){
  return {
    list: function(callback){
      $http.get('/api/').success(callback);
    }
  };
});