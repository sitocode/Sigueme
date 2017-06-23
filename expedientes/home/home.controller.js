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
          vm.dataLoading = true;
          ProcessFileService.GetAll(this.selectedConv)
              .then(function (expedientes) {$rootScope.gridOptions.data= expedientes.expedientes;vm.dataLoading = false;});
        };



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
              { field: 'CENTROS', headerCellClass: $rootScope.highlightFilteredHeader },
              { field: 'ESTADO', headerCellClass: $rootScope.highlightFilteredHeader },
            ]
          };




        function initController() {
            loadSelectConvocatorias();
        }

        function loadSelectConvocatorias() {
          ConvocatoriaService.GetAll()
              .then(function (convocatorias) {
                  vm.allConvocatorias = convocatorias.convocatorias;
              });
        }


    }

})();
