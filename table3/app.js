var app = angular.module('app', ['ngTouch', 'ui.grid']);

app.controller('MainCtrl', ['$scope','$http', function ($scope, $http) {



$http.get('/sigueme/API/expedientes/1')
  .success(function(data) {
    $scope.gridOptions.data = data.expedientes;
    console.log(data)
  });

$scope.columns = [{ field: 'CODIGOMINISTERIO' }, { field: 'TITULO' }, { field: 'ESTADO' }];
  $scope.gridOptions = {
    enableSorting: true,
    columnDefs: $scope.columns,
    onRegisterApi: function( gridApi ) {
      $scope.gridApi = gridApi;
      //var cellTemplate = 'ui-grid/selectionRowHeader';   // you could use your own template here
      //$scope.gridApi.core.addRowHeaderColumn( { name: 'rowHeaderCol', displayName: '', width: 30, cellTemplate: cellTemplate} );
      $scope.gridApi.core.addRowHeaderColumn( { name: 'rowHeaderCol', displayName: '', width: 30} );
    }
  };


}]);
