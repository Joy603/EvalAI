(function() {
    
        'use strict';
        angular
            .module('evalai')
            .controller('NotebookListCtrl', NotebookListCtrl);

        NotebookListCtrl.$inject = ['utilities'];
            
            function NotebookListCtrl(utilities) {
                var vm = this;
                var userKey = utilities.getData('userKey');

                vm.currentList = {};

                var parameters = {};
                // TODO Change for Notebooks
                parameters.url = 'challenges/challenge/present';
                parameters.method = 'GET';
                parameters.token = userKey;
            }
})();