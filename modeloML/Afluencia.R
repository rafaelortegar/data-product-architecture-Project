directorio <- '/home/alfie-gonzalez/Documentos/Maestría/Segundo Semestre/Métodos de Gran Escala/'
setwd(directorio)

library(tidyverse)

datos <- read_csv('afluencia-diaria-del-metro-cdmx.csv', 
                  col_types = cols(Fecha = col_character()))

datos %>% dim()

datos %>% complete.cases() %>% which.min()
datos[-287589,] %>% complete.cases() %>% which.min()
datos[287589,]
datos[409134,]

library(lubridate)

#extraer_dia <- function(x){
#  dia <- substr(x, 9, 10)
#  return(as.numeric(dia))
#}

#extraer_mes <- function(x){
#  mes <- substr(x, 6, 7)
#  return(as.numeric(mes))
#}

extraer_mes <- function(x){
  y <- which(x == c('enero', 'febrero', 'marzo', 'abril', 
                    'mayo', 'junio', 'julio', 'agosto', 
                    'septiembre', 'octubre', 'noviembre', 
                    'diciembre'))
  return(y)
}

#dia_semana <- function(x){
#  u <- wday(x, week_start = getOption("lubridate.week.start", 1))
#  return(u)
#}

datos_dep <- datos %>% 
  drop_na() %>% 
  #mutate(Fecha = as.character(Fecha)) %>% 
  #mutate(Fecha = as.Date(Fecha, format = "%Y-%d-%m")) %>% 
  #mutate(fecha2=make_date(Año, Mes, Dia)) %>% 
  mutate(Mes = map_chr(Mes, extraer_mes)) %>% 
  mutate(Fecha = make_date(year = Año, month = Mes, day = Dia)) %>% 
  mutate(dia_semana = wday(Fecha, 
                           week_start = getOption("lubridate.week.start", 
                                                  1))) %>% 
  mutate(Dia = factor(Dia), 
         Mes = factor(Mes), 
         Linea = factor(Linea),
         Estacion = factor(Estacion), 
         dia_semana = factor(dia_semana))

#EDA

datos_dep$Linea %>% unique()
datos_dep$Linea %>% unique() %>% length()

get_sample <- function(x, y){
  return(which(y$Dia == x)[1])
}

library(purrr)

#extra_indices <- map_dbl(1:31, ~get_sample(.x, datos_dep))

X <- datos_dep %>% select(-Afluencia)
y <- datos_dep$Afluencia

set.seed(123)
indices_ent <- sample(1:nrow(X), 
                      floor(0.50*nrow(X)), FALSE)
indices_val <- sample(setdiff(1:nrow(X), indices_ent), 
                      floor(0.50*length(indices_ent)), FALSE)
indices_pr <- (1:nrow(X))[-c(indices_ent, indices_val)]
x_ent <- X[indices_ent,]
x_val <- X[indices_val,]
x_pr <- X[indices_pr,]
y_ent <- y[indices_ent]
y_val <- y[indices_val]
y_pr <- y[indices_pr]

#indices_ent <- 1:floor(0.50*nrow(datos_dep))
#indices_val <- (floor(0.50*nrow(datos_dep))+1):floor(0.75*nrow(datos_dep))
#indices_ent <- floor(0.75*nrow(datos_dep)):nrow(floor())

rmse <- function(y, pred){
  return(sqrt(mean((y-pred)^2)))
}

#Regresión

modelo <- lm(y_ent ~ Dia+Mes+Linea+Estacion+dia_semana, data = x_ent)
pred_val <- predict(modelo, x_val)

datos_dep$Fecha %>% is.na() %>% sum()

rmse(y_val, pred_val)

#Ridge

x_mat <- model.matrix(y ~ ., data = X) %>% 
  as.data.frame()

library(glmnet)

cv_mod <- cv.glmnet(as.matrix(x_ent), y_ent, 
                    alpha = 0,
                    lambda = exp(seq(-12, 2, 0.5)))

lambda.min <- cv_mod$lambda.min

modelo_ridge <- glmnet(as.matrix(x_ent), y_ent, 
                       alpha = 0, 
                       lambda = lambda.min)

pred <- predict(modelo_ridge, as.matrix(x_val))
pred_ridge<-pred

rmse(y_val, pred_ridge)

