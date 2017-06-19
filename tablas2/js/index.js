angular.module('sortApp', [])

.controller('mainController', function($scope,$http) {
  $scope.sortType     = 'CODIGOMINISTERIO'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  $scope.searchTITULO   = '';     // set the default search/filter term

  // create the list of sushi rolls

  $scope.sushi=$http.get('/sigueme/API/expedientes/5').then(function(res){
    //params.total(res.data.inlineCount);
    return res.data.expedientes;
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
