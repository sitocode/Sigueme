(function () {
    'use strict';

    angular
        .module('app')
        .factory('ConvocatoriaService', ConvocatoriaService);

    ConvocatoriaService.$inject = ['$http'];
    function ConvocatoriaService($http) {
        var service = {};

        service.GetAll = GetAll;

        return service;

        function GetAll() {
            return $http.get('/sigueme/API/convocatorias').then(handleSuccess, handleError('Error getting all ProcessFiles'));
        }

        // private functions

        function handleSuccess(res) {
            return res.data;
        }

        function handleError(error) {
            return function () {
                return { success: false, message: error };
            };
        }
    }

})();
