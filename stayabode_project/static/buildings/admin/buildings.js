(function($) {
    $(document).ready(function() {
        console.log($.fn.jquery);
        if(!$("input[name='buildings']:checkbox:checked").length){
            $($("#id_residents option")).hide();
        }
        $("#id_buildings li").on('change', function(event) {
            var buildingId = event.target.getAttribute('value');
            $.get( "/building/get-residents", {id: buildingId}).done(function(residents){
                if (event.target.checked){
                    addResidentsToAvailableResidents(residents);
                }else{
                    removeResidents(residents);
                }
            });
        });

        function addResidentsToAvailableResidents(residents){
            residents.res.forEach(function(resident){
               $($("#id_residents option[value="+resident.id+"]")).show();
            })
        }

        function removeResidents(residents){
            // update available residents
            residents.res.forEach(function(resident){
                $($("#id_residents option[value="+resident.id+"]")).trigger('click');
                $($("#id_residents option[value="+resident.id+"]")).hide();
            });
        }
    });
})(django.jQuery);
