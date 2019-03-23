Vue.component('woman_death', {
    template: '<canvas id="w_d"></canvas>'
});

Vue.component('man_death', {
    template: '<canvas id="m_d"></canvas>'
});
Vue.component('death_by_age', {
    template: '<canvas id="d_b_a"></canvas>'
});
Vue.component('woman_born', {
    template: '<canvas id="w_b"></canvas>'
});
Vue.component('man_born', {
    template: '<canvas id="m_b"></canvas>'
});

function graphic(x,y, id, type, fill = true, showLine = true) {
    var ctx = document.getElementById(id).getContext('2d');
    new Chart(ctx, {
        type: type,
        data: {
            // x
            labels: x,
            // y
            datasets: [{
                data: y,
                borderWidth: 1,
                fill: fill,
                pointRadius: 10,
                pointHoverRadius: 15,
                showLine: showLine// no line shown
            }]
        },
    });
}

var app;
app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        year: 1
    },
    mounted: function () {

    },
    methods: {
        chart_woman: () => {
            axios.get('/death/female').then(
                response => {
                    graphic(response.data.len, response.data.number_d, 'w_d', 'bar')
                }
            );

        },
        chart_man: () => {
            axios.get('/death/male').then(
                response => {
                    graphic(response.data.len, response.data.number_d, 'm_d', 'bar')
                }
            );

        },
        borns_man: () => {
            axios.get('/born/male').then(
                response => {
                    graphic(response.data.len, response.data.number_d, 'm_b', 'line', false, false)
                }
            );
        },
        borns_woman: () => {
            axios.get('/born/female').then(
                response => {
                    graphic(response.data.len, response.data.number_d, 'w_b', 'line', false, false)
                }
            );
        },

        death_by_age: () => {
            axios.get('/deathbyage/' + app.year).then(
                response => {
                    graphic(response.data.x, response.data.data, 'd_b_a', 'line')
                }
            );

        },

        next_year: () => {
            app.year += 1;
            app.death_by_age()
        },

        prev_year: () => {
            if(app.year == 1){
                alert('Estas en el primer año de la simulacion')
            }
            else
                app.year -= 1
        }

    }
});


