angular.module('sortApp', [])

.controller('mainController', function($scope,$http) {
  $scope.sortType     = 'CODIGOMINISTERIO'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  $scope.searchTITULO   = '';     // set the default search/filter term


   $http.get('/sigueme/API/expedientes/1').then(function(res){
    $scope.sushi= res.data.expedientes;
  });

/*
  $scope.sushi = [
    { CODIGOMINISTERIO: 'Cali Roll', TITULO: 'Crab', ESTADO: '2' },
    { CODIGOMINISTERIO: 'Philly', TITULO: 'Tuna', ESTADO: '4' },
    { CODIGOMINISTERIO: 'Tiger', TITULO: 'Eel', ESTADO: '7' },
    { CODIGOMINISTERIO: 'Rainbow', TITULO: 'Variety', ESTADO: '6' }
  ];
*/

});
