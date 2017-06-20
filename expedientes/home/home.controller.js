﻿(function () {
    'use strict';

    angular
        .module('app')
        .controller('HomeController', HomeController);

    HomeController.$inject = ['ProcessFileService', 'ConvocatoriaService', 'NgTableParams','$rootScope', '$http'];

    function HomeController(ProcessFileService, ConvocatoriaService, NgTableParams, $rootScope, $http) {
        var vm = this;
        vm.allExpedientes = [];
        vm.allConvocatorias = [];

        initController();


        $rootScope.cambio = function() {
          ProcessFileService.GetAll(this.selectedConv)
              .then(function (expedientes) {vm.allExpedientes = expedientes.expedientes;});
        };

        $http.get('/sigueme/API/expedientes/5').then(function(res){
         $rootScope.prueba= JSON.parse(res.data.expedientes);
       });


        //var data = [{"CODIGOMINISTERIO": "Moroni", "TITULO": "Moroni","ESTADO": "Moroni"},{"CODIGOMINISTERIO": "Moroni2", "TITULO": "Moroni2","ESTADO": "Moroni2"}];

        var data= $rootScope.prueba;

        this.tableParams = new NgTableParams({}, {
          dataset: data
        });


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
