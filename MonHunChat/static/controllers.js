ChatControllers.controller('ChatListCtrl', ['$scope', '$dragon', function ($scope, $dragon) {
    $scope.chatList = {};
    $scope.chatItems = [];
    $scope.channel = 'chats';

    $dragon.onReady(function() {
        $dragon.subscribe('chat-item', $scope.channel, {chat_list__id: 1}).then(function(response) {
            $scope.dataMapper = new DataMapper(response.data);
        });

        $dragon.getSingle('chat-list', {id:1}).then(function(response) {
            $scope.chatList = response.data;
        });

        $dragon.getList('chat-item', {list_id:1}).then(function(response) {
            $scope.chatItems = response.data;
        });
    });

    $dragon.onChannelMessage(function(channels, message) {
        if (indexOf.call(channels, $scope.channel) > -1) {
            $scope.$apply(function() {
                $scope.dataMapper.mapData($scope.chatItems, message);
            });
        }
    });

    $scope.itemDone = function(item) {
        item.done = true != item.done;
        $dragon.update('chat-item', item);
    }
}]);
