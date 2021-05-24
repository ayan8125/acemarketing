function pull_Date() {
    today_date = document.getElementById('t-date');
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           // Typical action to be performed when the document is ready:
           var responsedata = JSON.parse(this.response)
           today_date.innerHTML = responsedata.date
        }
    };
    xhttp.open("GET", '/user/give_date/', true);
    xhttp.send();

}



function make_request(url, result_to_dispatch_At_Id) {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           // Typical action to be performed when the document is ready:
           var responsedata = JSON.parse(this.response)
           if (responsedata.serach_engine_reachs) {
               const data = {
                    labels: ['Serach Engine Reachs', 'Social Media Reachs'],
                    datasets: [
                        {
                            label: 'Search Engine and Social Medias Reachs',
                            data: [responsedata.serach_engine_reachs.total_reach, responsedata.social_media_reachs.total_reach],
                            backgroundColor: ['rgba(220,20,60,1)', 'rgb(0,191,255,1)'],
                        }
                    ]
                };
               drawChart('doughnut', 'reachChart',data, 'Reachs','total-reach')
                        var overall_reach = (responsedata.serach_engine_reachs.total_reach + responsedata.social_media_reachs.total_reach)
                       var reach_data_area = document.getElementById('total-reach')
                       reach_data_area.innerHTML = overall_reach
           }
           else{
               const data = {
                    labels: ['Serach engine Clicks', 'Social Media Clicks'],
                    datasets: [
                        {
                            label: 'Search Engine and Social Medias Clicks',
                            data: [responsedata.serach_engine_clicks.total_clicks, responsedata.social_media_clicks.total_clicks],
                            backgroundColor: ['rgba(220,20,60,1)', 'rgb(0,191,255,1)'],
                        }
                    ]
                };
               drawChart('doughnut', 'clicksChart',data, 'Clicks','total-clicks')
               var overall_clicks = (responsedata.serach_engine_clicks.total_clicks + responsedata.social_media_clicks.total_clicks)
                var clicks_data_area = document.getElementById('total-clicks')
                clicks_data_area.innerHTML = overall_clicks
           }

           

        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();

}


function drawChart(type, chart_to_dipatch_at_id, data, title) {
    var ctx = document.getElementById(chart_to_dipatch_at_id).getContext('2d');
    var myChart = new Chart(ctx, {
    type: type,
    data: data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                       font: {
                        size: 14
                    }
                }
            },
            title: {
                display: true,
                text: title
            }
        }
    },
});


}


function get_content(url, dispatch_id) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        // Typical action to be performed when the document is ready:
        document.getElementById(dispatch_id).innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();

}

pull_Date();
make_request('/user/get-social-and-engine-reachs/', 'my-reach-chart');
make_request('/user/get-social-and-engine-clicks/', 'my-clicks-chart');
get_content('/user/get-campaign-reach-clicks-info/', 'camp-info-block');

