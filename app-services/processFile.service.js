(function () {
    'use strict';

    angular
        .module('app')
        .factory('ProcessFileService', ProcessFileService);

    ProcessFileService.$inject = ['$http'];
    function ProcessFileService($http) {
        var service = {};

        service.GetAll = GetAll;

        return service;

        function GetAll(id) {
            return $http.get('/sigueme/API/expedientes/'+id).then(handleSuccess, handleError('Error getting all ProcessFiles'));
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
