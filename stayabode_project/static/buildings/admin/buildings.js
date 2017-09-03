(function($) {
    $(document).ready(function() {
    $($("#id_residents option")).hide();
        var selectedBuildings = $('input:checkbox:checked').map(function() {
            return this.value;
        }).get();

        if(selectedBuildings.length){
            $.get( "/building/get-residents", {ids: selectedBuildings}).done(function(response){
                response.residents.forEach(function(resident){
                   $($("#id_residents option[value="+resident.id+"]")).show();
                })
            });
        }

        $("#id_buildings li").on('change', function(event) {
            var buildingId = event.target.getAttribute('value');
            $.get( "/building/get-residents", {ids: [buildingId]}).done(function(response){
                if (event.target.checked){
                    addResidentsToAvailableResidents(response);
                }else{
                    removeResidents(response);
                }
            });
        });

        function addResidentsToAvailableResidents(response){
            response.residents.forEach(function(resident){
               $($("#id_residents option[value="+resident.id+"]")).show();
            })
        }

        function removeResidents(response){
            // update available residents
            response.residents.forEach(function(resident){
                $($("#id_residents option[value="+resident.id+"]")).hide();
            });
        }
    });
})(django.jQuery);
