var app = angular.module("myApp", ["ngTable", "ngResource", "ngTableDemoFakeBackend"]);
(function() {

  app.controller("demoController", demoController);
  demoController.$inject = ["NgTableParams", "$resource"];

  function demoController(NgTableParams, $resource) {
    // tip: to debug, open chrome dev tools and uncomment the following line 
    //debugger;
    
    var Api = $resource("/data");
    this.tableParams = new NgTableParams({}, {
      getData: function(params) {
        // ajax request to api
        return Api.get(params.url()).$promise.then(function(data) {
          params.total(data.inlineCount); // recal. page nav controls
          return data.results;
        });
      }
    });
  }
})();