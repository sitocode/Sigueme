(function () {
    'use strict';

    angular
        .module('app')
        .controller('HomeController', HomeController);

    HomeController.$inject = ['ProcessFileService', 'ConvocatoriaService', 'NgTableParams','$rootScope'];

    function HomeController(ProcessFileService, ConvocatoriaService, NgTableParams, $rootScope) {
        var vm = this;
        vm.allExpedientes = [];
        vm.allConvocatorias = [];

        initController();

        $rootScope.cambio = function() {
          ProcessFileService.GetAll(this.selectedConv)
              .then(function (expedientes) {
                  vm.allExpedientes = expedientes.expedientes;
              });
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


        function loadAllExpedientes(idconvocatoria) {
            ProcessFileService.GetAll(idconvocatoria)
                .then(function (expedientes) {
                    vm.allExpedientes = expedientes.expedientes;
                });
        }

    }

})();
