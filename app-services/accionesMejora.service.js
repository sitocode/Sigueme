(function () {
    'use strict';

    angular
        .module('app')
        .factory('AccionesMejoraService', AccionesMejoraService);

    AccionesMejoraService.$inject = ['$http'];
    function AccionesMejoraService($http) {
        var service = {};

        service.GetAll = GetAll;

        return service;

        function Get(idtitulo,idconvocatoria) {
            return $http.get('/sigueme/API/amejora/'+idtitulo+'/'+idconvocatoria).then(handleSuccess, handleError('Error getting all ProcessFiles'));
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
