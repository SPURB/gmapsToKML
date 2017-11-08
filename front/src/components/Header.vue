<template>
    <div class=row>
        <div id="intro" class='twelve columns'>
            <h5>{{title}}</h5>
             <p>Fonte: <a href="https://developers.google.com/maps/documentation/javascript/places/" target="blank">API Google Maps Places</a></p>
        </div>
    </div>
</template>
<script>
export default{
    data: function(){
        return{
            title:"Conversão de locais definidos na API do google maps em KML"
        }
    }
}    
</script>