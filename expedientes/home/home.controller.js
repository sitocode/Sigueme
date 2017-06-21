(function () {
    'use strict';

    angular
        .module('app')
        .controller('HomeController', HomeController);

    HomeController.$inject = ['ProcessFileService', 'ConvocatoriaService','$rootScope', '$http'];

    function HomeController(ProcessFileService, ConvocatoriaService, $rootScope, $http) {
        var vm = this;
        vm.allExpedientes = [];
        vm.allConvocatorias = [];

        initController();


        $rootScope.cambio = function() {
          ProcessFileService.GetAll(this.selectedConv)
              .then(function (expedientes) {vm.allExpedientes = expedientes.expedientes;});
        };

<<<<<<< HEAD
        $rootScope.cambio = function() {
          ProcessFileService.GetAll(this.selectedConv)
              .then(function (expedientes) {$rootScope.gridOptions.data= expedientes.expedientes;});
        };


        $http.get('/sigueme/API/expedientes/5').then(function(res){
         $rootScope.gridOptions.data= res.data.expedientes;
        });


        //$rootScope.columns = [{ field: 'CODIGOMINISTERIO' }, { field: 'TITULO' },{ field: 'UNIVERSIDAD' }, { field: 'ESTADO' }];

/*
          $rootScope.gridOptions = {
            enableSorting: true,
            columnDefs: $rootScope.columns,
            onRegisterApi: function( gridApi ) {
              $rootScope.gridApi = gridApi;
              $rootScope.gridApi.core.addRowHeaderColumn( { name: 'rowHeaderCol', displayName: '', width: 30} );
            }
          };
*/

    $rootScope.highlightFilteredHeader = function( row, rowRenderIndex, col, colRenderIndex ) {
  if( col.filters[0].term ){
    return 'header-filtered';
  } else {
    return '';
  }
};
          $rootScope.gridOptions = {
            enableFiltering: true,
            onRegisterApi: function(gridApi){
              $rootScope.gridApi = gridApi;
            },
            columnDefs: [
              // default
              { field: 'CODIGOMINISTERIO', headerCellClass: $rootScope.highlightFilteredHeader },
              { field: 'TITULO', headerCellClass: $rootScope.highlightFilteredHeader },
              { field: 'UNIVERSIDAD', headerCellClass: $rootScope.highlightFilteredHeader },
              { field: 'ESTADO', headerCellClass: $rootScope.highlightFilteredHeader },
            ]
          };













=======
        $http.get('/sigueme/API/expedientes/5').then(function(res){
         $rootScope.prueba= JSON.parse(res.data.expedientes);
       });


        //var data = [{"CODIGOMINISTERIO": "Moroni", "TITULO": "Moroni","ESTADO": "Moroni"},{"CODIGOMINISTERIO": "Moroni2", "TITULO": "Moroni2","ESTADO": "Moroni2"}];

        var data= $rootScope.prueba;

        this.tableParams = new NgTableParams({}, {
          dataset: data
        });
>>>>>>> 97f0465e2d7dae486087b2109d2da3e0098ba505


        function initController() {
            loadSelectConvocatorias();
        }

        function loadSelectConvocatorias() {
          ConvocatoriaService.GetAll()
              .then(function (convocatorias) {
                  vm.allConvocatorias = convocatorias.convocatorias;
              });
        }


        function loadAllExpedientes(idconvocatoria) {
            ProcessFileService.GetAll(idconvocatoria)
                .then(function (expedientes) {
                    vm.allExpedientes = expedientes.expedientes;

                });
        }

    }

})();
