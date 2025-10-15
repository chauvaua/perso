# app.R
library(shiny)
library(shinydashboard)
library(dplyr)
library(ggplot2)
library(DT)

# dataset d'exemple : mtcars
data0 <- mtcars
data0$model <- rownames(mtcars)

ui <- dashboardPage(
  dashboardHeader(title = "Dashboard Shiny - exemples d'indicateurs"),
  dashboardSidebar(
    selectInput("cyl", "Filtrer par cylindre :", choices = c("Tous", sort(unique(data0$cyl))), selected = "Tous")
  ),
  dashboardBody(
    fluidRow(
      valueBoxOutput("nb"),
      valueBoxOutput("avg_mpg"),
      valueBoxOutput("max_hp")
    ),
    fluidRow(
      box(title = "Scatter MPG vs HP", status = "primary", solidHeader = TRUE, width = 8,
          plotOutput("scatter", height = 300)
      ),
      box(title = "Données (filtrées)", status = "info", solidHeader = TRUE, width = 4,
          DT::dataTableOutput("table")
      )
    )
  )
)

server <- function(input, output, session) {
  
  # données réactives selon le filtre
  df <- reactive({
    if (input$cyl == "Tous") data0 else filter(data0, cyl == as.numeric(input$cyl))
  })
  
  # indicateurs
  output$nb <- renderValueBox({
    valueBox(value = nrow(df()), subtitle = "Nombre d'observations", icon = icon("table"), color = "aqua")
  })
  output$avg_mpg <- renderValueBox({
    valueBox(value = ifelse(nrow(df())>0, round(mean(df()$mpg), 2), NA), subtitle = "MPG moyen", icon = icon("tachometer-alt"), color = "green")
  })
  output$max_hp <- renderValueBox({
    valueBox(value = ifelse(nrow(df())>0, max(df()$hp), NA), subtitle = "Puissance max (hp)", icon = icon("bolt"), color = "yellow")
  })
  
  # graphique
  output$scatter <- renderPlot({
    ggplot(df(), aes(x = hp, y = mpg)) +
      geom_point(size = 3) +
      labs(x = "Chevaux (hp)", y = "MPG") +
      theme_minimal()
  })
  
  # table
  output$table <- DT::renderDataTable({
    DT::datatable(df()[, c("model","mpg","hp","cyl")], options = list(pageLength = 5))
  })
}

shinyApp(ui, server)