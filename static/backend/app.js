var app = angular.module("myApp", [])

app.controller("myCtrl", function($scope, $http) {

$scope.genersdata = [];
$scope.halldata = [];
$scope.moviedata = [];

$http({
		url:"movie/fetchdata"
	}).success(function (data)
    {
        $scope.genersdata=data;
        //demoService.SetData(1);
        //demoService1.SetData(1);
          
    });


$http({
		url:"movie/fetchdatahall"
	}).success(function (data)
    {
        $scope.halldata=data;
        //demoService.SetData(1);
        //demoService1.SetData(1);
          
    });

$http({
		url:"movie/fetchmoviedata"
	}).success(function (data)
    {
        $scope.moviedata=data;
        //console.log(data);
        //demoService.SetData(1);
        //demoService1.SetData(1);
          
    });
});