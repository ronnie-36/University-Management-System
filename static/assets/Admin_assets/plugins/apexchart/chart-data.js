"use strict";

$(document).ready(function () {
  // Area chart

  var options = {
    chart: {
      height: 350,
      type: "area",
      toolbar: {
        show: false,
      },
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: "smooth",
    },
    series: [
      {
        name: "Sales",
        data: [45, 60, 75, 51, 42, 42, 30],
      },
      {
        name: "Expenses",
        color: "#FFBC53",
        data: [24, 48, 56, 32, 34, 52, 25],
      },
    ],
    xaxis: {
      categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    },
  };
  var chart = new ApexCharts(
    document.querySelector("#apexcharts-area"),
    options
  );
  chart.render();

  // Bar chart

  var optionsBar = {
    chart: {
      type: "bar",
      height: 350,
      width: "100%",
      stacked: true,
      toolbar: {
        show: false,
      },
    },
    dataLabels: {
      enabled: false,
    },
    plotOptions: {
      bar: {
        columnWidth: "50%",
      },
    },
    series: [
      {
        name: "Master Degree",
        color: "#fdbb38",
        data: [
          420,
          532,
          516,
          575,
          454,
          392,
          262,
          383,
          446,
          551,
          563,
          421,
          563,
          254,
          452,
        ],
      },
      {
        name: "Bachlor Degree",
        color: "#19affb",
        data: [
          436,
          512,
          444,
          663,
          456,
          544,
          523,
          600,
          655,
          756,
          726,
          852,
          925,
          1025,
          1136,
        ],
      },
    ],
    labels: [
      2007,
      2008,
      2009,
      2010,
      2011,
      2012,
      2013,
      2014,
      2015,
      2016,
      2017,
      2018,
      2019,
      2020,
      2021,
    ],
    xaxis: {
      labels: {
        show: false,
      },
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
    },
    yaxis: {
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
      labels: {
        style: {
          colors: "#777",
        },
      },
    },
    title: {
      text: "",
      align: "left",
      style: {
        fontSize: "18px",
      },
    },
  };

  var chartBar = new ApexCharts(document.querySelector("#bar"), optionsBar);
  chartBar.render();
});
