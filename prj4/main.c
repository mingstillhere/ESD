/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2020 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "cmsis_os.h"
#include "queue.h"
#include "semphr.h"
/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
osThreadId Task01Handle;
osThreadId Task02Handle;
osThreadId Task03Handle;
osMessageQId myQueue01Handle;
osMessageQId myQueue02Handle;
SemaphoreHandle_t xSemaphore;
BaseType_t xHigherPriorityTaskWoken;
/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
void StartDefaultTask(void const * argument);
void StartTask02(void const * argument);
void StartTask03(void const * argument);

/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */
  xSemaphore = xSemaphoreCreateBinary();

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */
  xHigherPriorityTaskWoken=pdFALSE;

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  /* USER CODE BEGIN 2 */

  /* USER CODE END 2 */

  /* USER CODE BEGIN RTOS_MUTEX */
  /* add mutexes, ... */
  /* USER CODE END RTOS_MUTEX */

  /* USER CODE BEGIN RTOS_SEMAPHORES */
  /* add semaphores, ... */
  /* USER CODE END RTOS_SEMAPHORES */

  /* USER CODE BEGIN RTOS_TIMERS */
  /* start timers, add new ones, ... */
  /* USER CODE END RTOS_TIMERS */

  /* Create the queue(s) */
  /* definition and creation of myQueue01 */
  osMessageQDef(myQueue01, 8, int16_t);
  myQueue01Handle = osMessageCreate(osMessageQ(myQueue01), NULL);

  /* definition and creation of myQueue02 */
  osMessageQDef(myQueue02, 8, int16_t);
  myQueue02Handle = osMessageCreate(osMessageQ(myQueue02), NULL);

  /* USER CODE BEGIN RTOS_QUEUES */
  /* add queues, ... */
  /* USER CODE END RTOS_QUEUES */

  /* Create the thread(s) */
  /* definition and creation of Task01 */
  osThreadDef(Task01, StartDefaultTask, osPriorityNormal, 0, 128);
  Task01Handle = osThreadCreate(osThread(Task01), NULL);

  /* definition and creation of Task02 */
  osThreadDef(Task02, StartTask02, osPriorityNormal, 0, 128);
  Task02Handle = osThreadCreate(osThread(Task02), NULL);

  /* definition and creation of Task03 */
  osThreadDef(Task03, StartTask03, osPriorityNormal, 0, 128);
  Task03Handle = osThreadCreate(osThread(Task03), NULL);

  /* USER CODE BEGIN RTOS_THREADS */
  /* add threads, ... */
  /* USER CODE END RTOS_THREADS */

  /* Start scheduler */
  osKernelStart();

  /* We should never get here as control is now taken by the scheduler */
  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE3);
  /** Initializes the CPU, AHB and APB busses clocks
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB busses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_HSI;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_7, GPIO_PIN_RESET);

  /*Configure GPIO pin : PB7 */
  GPIO_InitStruct.Pin = GPIO_PIN_7;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/* USER CODE BEGIN Header_StartDefaultTask */
/**
  * @brief  Function implementing the Task01 thread.
  * @param  argument: Not used
  * @retval None
  */
/* USER CODE END Header_StartDefaultTask */
void StartDefaultTask(void const * argument)
{
  /* USER CODE BEGIN 5 */
  /* Infinite loop */
	int16_t num = 0;
	for(;;)
	{
		HAL_Delay(1000);
		num++;
		xQueueSend(myQueue01Handle, ( void* )&num, portMAX_DELAY);
		HAL_Delay(1000);
		num++;
		xQueueSend(myQueue01Handle, ( void* )&num, portMAX_DELAY);
		xQueueSend(myQueue02Handle, ( void* )&num, portMAX_DELAY);
	  }
  /* USER CODE END 5 */
}

/* USER CODE BEGIN Header_StartTask02 */
/**
* @brief Function implementing the Task02 thread.
* @param argument: Not used
* @retval None
*/
/* USER CODE END Header_StartTask02 */
void StartTask02(void const * argument)
{
  /* USER CODE BEGIN StartTask02 */
  /* Infinite loop */
	int16_t rec_num;
	  for(;;)
	  {
		  if ( xQueueReceive(myQueue01Handle,&(rec_num),portMAX_DELAY) == pdPASS)
			  {
			  	 xSemaphoreGiveFromISR( xSemaphore, &xHigherPriorityTaskWoken  );
			  	 portYIELD_FROM_ISR( xHigherPriorityTaskWoken );

				 while(rec_num>0)
				 {
					  HAL_GPIO_TogglePin(GPIOB, GPIO_PIN_7);
					  HAL_Delay(500);
					  rec_num--;
				 }
				 xSemaphoreTake( xSemaphore, portMAX_DELAY );
			  }
	  }
  /* USER CODE END StartTask02 */
}

/* USER CODE BEGIN Header_StartTask03 */
/**
* @brief Function implementing the Task03 thread.
* @param argument: Not used
* @retval None
*/
/* USER CODE END Header_StartTask03 */
void StartTask03(void const * argument)
{
  /* USER CODE BEGIN StartTask03 */
  /* Infinite loop */
	int16_t rec_num;
		  for(;;)
		  {
			  if ( xQueueReceive(myQueue02Handle,&(rec_num),portMAX_DELAY) == pdPASS)
				  {
				  	  xSemaphoreTake( xSemaphore, portMAX_DELAY );
				  	  portYIELD_FROM_ISR( xHigherPriorityTaskWoken );

					  while(rec_num>0)
					  {
						   HAL_GPIO_TogglePin(GPIOB, GPIO_PIN_7);
						   HAL_Delay(500);
						   rec_num--;
					  }
					  xSemaphoreGiveFromISR( xSemaphore, &xHigherPriorityTaskWoken  );
					  portYIELD_FROM_ISR( xHigherPriorityTaskWoken );
				  }
		  }
  /* USER CODE END StartTask03 */
}

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */

  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     tex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
